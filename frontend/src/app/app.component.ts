import { Component } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Chart, registerables } from 'chart.js';

// Registrar os módulos do Chart.js
Chart.register(...registerables);

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HttpClientModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  query: string = '';
  resultados: any[] = [];
  carregando: boolean = false;
  isDarkMode: boolean = false;
  
  // Modais e Dados
  exibirModal: boolean = false;
  exibirModalVendas: boolean = false;
  dadosVendas: any = null;
  
  // Instância do Gráfico
  chart: any;

  constructor(private http: HttpClient) {}

  toggleDarkMode() {
    this.isDarkMode = !this.isDarkMode;
    document.body.classList.toggle('dark-theme', this.isDarkMode);
  }

  buscar() {
    if (!this.query.trim()) return;
    this.carregando = true;
    
    // Busca inicial na API de produtos
    this.http.get<any[]>(`http://localhost:8000/api/search?q=${this.query}`)
      .subscribe({
        next: (res) => {
          this.resultados = res;
          this.carregando = false;
        },
        error: (err) => {
          console.error('Erro na busca:', err);
          this.carregando = false;
        }
      });
  }

  abrirLink(url: string) {
    if (url && url !== '#') {
      window.open(url, '_blank', 'noopener noreferrer');
    } else {
      alert('Link não disponível para este produto.');
    }
  }

  // Lógica do Botão "📊 Preços"
  analisarPrecos(nome: string) {
    this.exibirModal = true; // Abre o modal para o Canvas existir no DOM
    
    this.http.get(`http://localhost:8000/api/analise-produto?q=${nome}`)
      .subscribe({
        next: (res: any) => {
          console.log('Dados para o gráfico:', res);
          // O segredo: setTimeout garante que o Angular desenhou o canvas antes de criar o gráfico
          setTimeout(() => {
            this.renderizarGrafico(res);
          }, 300);
        },
        error: (err) => console.error('Erro ao buscar dados do gráfico:', err)
      });
  }

  // Lógica do Botão "🤝 Comparação"
  compararMercado(nome: string) {
    this.exibirModalVendas = true;
    this.http.get(`http://localhost:8000/api/comparar-vendas?q=${nome}`)
      .subscribe({
        next: (res: any) => {
          this.dadosVendas = res;
          console.log('Métricas de mercado:', res);
        },
        error: (err) => console.error('Erro ao comparar vendas:', err)
      });
  }

  renderizarGrafico(dados: any) {
    const canvas = document.getElementById('graficoPrecos') as HTMLCanvasElement;
    
    if (!canvas) {
      console.error('Canvas não encontrado! Verifique se o ID está correto no HTML.');
      return;
    }

    // Destruir gráfico antigo para evitar sobreposição
    if (this.chart) {
      this.chart.destroy();
    }

    // Criar o novo gráfico com os dados do Python
    this.chart = new Chart(canvas, {
      type: 'bar',
      data: {
        labels: dados.labels, // Lojas (ex: Havan, Kabum)
        datasets: [{
          label: 'Preço R$',
          data: dados.valores, // Preços unitários
          backgroundColor: 'rgba(93, 63, 211, 0.7)',
          borderColor: 'rgba(93, 63, 211, 1)',
          borderWidth: 2,
          borderRadius: 8
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false }
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: (value) => 'R$ ' + value
            }
          }
        }
      }
    });
  }
}