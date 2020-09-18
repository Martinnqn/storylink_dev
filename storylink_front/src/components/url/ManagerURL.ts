import { reverse } from "named-urls";

class ManagerURL {
  private backendURL: string;

  constructor(backendURL: string) {
    this.backendURL = backendURL;
  }

  public getPath(url: string, params: JSON = JSON.parse("{}")) {
    return reverse(`${this.backendURL}${url}`, params);
  }
}

export default ManagerURL;
