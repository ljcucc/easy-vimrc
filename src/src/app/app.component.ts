import { Component } from '@angular/core';
declare var window: any;


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'src';
}

export const eel = window.eel
eel.set_host('ws://localhost:8000')
eel.helloworld()