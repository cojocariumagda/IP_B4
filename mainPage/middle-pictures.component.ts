import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-middle-pictures',
  templateUrl: './middle-pictures.component.html',
  styleUrls: ['./middle-pictures.component.css']
})
export class MiddlePicturesComponent implements OnInit {
  imageObject: Array<object> = [{ image: 'https://images.medicaldaily.com/sites/medicaldaily.com/files/styles/headline/public/2014/06/04/viagra.jpg', thumbImage: 'https://images.medicaldaily.com/sites/medicaldaily.com/files/styles/headline/public/2014/06/04/viagra.jpg'},
    { image: 'https://s25562.pcdn.co/wp-content/uploads/2015/08/iStock_000058886334_Medium.jpg', thumbImage: 'https://s25562.pcdn.co/wp-content/uploads/2015/08/iStock_000058886334_Medium.jpg'},
    {image: 'https://www.canadahealthcaremall.com/wp-content/uploads/2016/08/medical-pills.jpg', thumbImage: 'https://www.canadahealthcaremall.com/wp-content/uploads/2016/08/medical-pills.jpg'}];
  constructor() {}

  ngOnInit(): void {
  }

}
