import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TomorrowService {
  // readonly ROOT_URL = 'https://jsonplaceholder.typicode.com';
  readonly ROOT_URL = 'http://localhost:3000';
  // readonly ROOT_URL = 'https://sunny-day-cycling.wl.r.appspot.com';

  constructor(private http: HttpClient) { }

  getData(loc: any) {
    let params = new HttpParams().set('loc', loc);
    // let params = new HttpParams().set('userId', uId);

    return this.http.get(this.ROOT_URL + '/api/weather', { params });
    // return this.http.get(this.ROOT_URL + '/posts', { params });
  }
}
