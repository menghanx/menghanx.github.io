import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpErrorResponse } from '@angular/common/http'
import { catchError, map, retry } from 'rxjs/operators';
import { Observable, throwError } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class AutocompleteService {

  readonly ROOT_URL = 'http://localhost:3000/api/auto';
  // readonly ROOT_URL = 'http://localhost:3000/api/weather?loc=40.758,-73.9855';

  constructor(private http: HttpClient) { }

  public getData(input: string) {
    let params = new HttpParams().set('input', input);
    return this.http.get(this.ROOT_URL, { params })
      .pipe(
        catchError(this.errorHandler)
      );
  }
  private errorHandler(error: HttpErrorResponse) {
    return throwError(error.message || "server error.");
  }
}
