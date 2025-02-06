import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Assistant IA';
  query = '';
  response = '';

  constructor(private http: HttpClient) { }

  sendQuery() {
    this.http.post<any>('http://localhost:5000/api/query', { query: this.query })
      .subscribe({
        next: (res) => { this.response = res.response; },
        error: (err) => { this.response = "Erreur lors de l'appel à l'API"; }
      });
  }
}
