import { TagContentType } from '@angular/compiler';
import { Component, OnInit } from '@angular/core';
import {PosTagService} from '../pos-tag.service'

@Component({
  selector: 'app-body',
  templateUrl: './body.component.html',
  styleUrls: ['./body.component.scss']
})
export class BodyComponent implements OnInit {
  state: string;
  posTags: any;
  ary: any;
  table = false;

  constructor(private PosTagService:PosTagService) { }

  ngOnInit(): void {
  }
  sendStatement() {
    console.log("input statement :", this.state);
    this.PosTagService.getTags(this.state).subscribe(
      data => this.posTags = data,
      error => console.error(error)
    )
    setTimeout(()=>{
      this.myFunction() 
    }, 100)
  }

   myFunction() {
     console.log("table data :", this.posTags);
    this.ary = this.posTags.POS_Tags
    this.table = true;
  }

}
