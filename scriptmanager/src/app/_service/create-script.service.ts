import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment'

@Injectable({
  providedIn: 'root'
})
export class CreateScriptService {
  public env =  environment;
  public apiUrl = this.env['apiUrlScript']

  public getScript(tid){
    const _url = `${this.apiUrl}/tutorial/${tid}/scripts/`
    return this.httpClient.get(_url);
  }

  public postScript(tid,data) {
    const _url = `${this.apiUrl}/tutorial/${tid}/scripts/`
    var ls = this.httpClient.post(
      _url,
      data
    );
    return ls;
  }

  public patchScript(tid,data) {
    const _url = `${this.apiUrl}/tutorial/${tid}/scripts/`
    var ls = this.httpClient.patch(
      _url,
      data
    );
    return ls;
  }

  public deleteScript(tid,srcipt_pk) {
    const _url = `${this.apiUrl}/tutorial/${tid}/scripts/${srcipt_pk}/`
    var ls = this.httpClient.delete(
      _url
    );
    return ls;
  }
  
  public getComment(tid){
    const _url = `${this.apiUrl}/scripts/${tid}/comments/`
    return this.httpClient.get(_url);
  }

  public postComment(tid,data) {
    const _url = `${this.apiUrl}/scripts/${tid}/comments/`
    var ls = this.httpClient.post(
      _url,
      data
    );
    return ls;
  }

  constructor(private httpClient: HttpClient) { }
}
