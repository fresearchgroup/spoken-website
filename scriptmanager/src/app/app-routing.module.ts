import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ScriptCreateComponent } from './script/script-create/script-create.component';
import { ScriptEditComponent } from './script/script-edit/script-edit.component';
import { ScriptViewComponent } from './script/script-view/script-view.component';
import { ScriptRevisionComponent } from './script/script-revision/script-revision.component';
import {ScriptUploadComponent } from './script/script-upload/script-upload.component'
import { AuthGuard } from './_guards/auth.guard';
const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    // canActivate: [AuthGuard],
    data: {
      title: 'List of Tutorials',
      animation: 'HomePage'
    }
  },
  {
    path: 'create/:tid/:lid/:tutorialName',
    component: ScriptCreateComponent,
    canActivate: [AuthGuard],
    data: {
      title: 'Create Script',
      animation: 'HomePage'
    }
  },
  {
    path: 'upload/:tid/:lid/:tutorialName',
    component: ScriptUploadComponent,
    canActivate: [AuthGuard],
    data: {
      title: 'Upload Script',
      animation: 'HomePage'
    }
  },

  {
    path: 'edit/:tid/:lid/:tutorialName',
    component: ScriptEditComponent,
    canActivate: [AuthGuard],
    data: {
      title: 'Edit Script',
      animation: 'HomePage'
    }
  },
  {
    path: 'view/:tid/:lid/:tutorialName',
    component: ScriptViewComponent,
    // canActivate: [AuthGuard],
    data: {
      title: 'View Script',
      animation: 'HomePage'
    }
  },
  {
    path: 'revisions',
    component: ScriptRevisionComponent,
    canActivate: [AuthGuard],
    data: {
      title: 'Revisions',
      animation: 'HomePage'
    }
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
