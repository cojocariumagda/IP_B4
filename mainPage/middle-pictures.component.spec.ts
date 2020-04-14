import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MiddlePicturesComponent } from './middle-pictures.component';

describe('MiddlePicturesComponent', () => {
  let component: MiddlePicturesComponent;
  let fixture: ComponentFixture<MiddlePicturesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MiddlePicturesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MiddlePicturesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
