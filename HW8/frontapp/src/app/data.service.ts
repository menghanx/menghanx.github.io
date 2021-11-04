import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs'


@Injectable({
  providedIn: 'root'
})
export class DataService {

  private dataSource = new BehaviorSubject<Object>({});
  currentData = this.dataSource.asObservable();

  private detail_data = new BehaviorSubject<Object>({});
  currentDetail = this.detail_data.asObservable();

  constructor() { }
  updateData(data: any) {
    this.dataSource.next(data);
  }

  updateDetail(data: any) {
    this.detail_data.next(data);
  }
}