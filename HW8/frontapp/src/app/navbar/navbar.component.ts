import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  res_selected = true;
  fav_selected = false;

  constructor() { }

  ngOnInit(): void {
  }

  selectRes() {
    this.res_selected = true;
    this.fav_selected = false;
  }

  selectFav() {
    this.res_selected = false;
    this.fav_selected = true;
  }
}
