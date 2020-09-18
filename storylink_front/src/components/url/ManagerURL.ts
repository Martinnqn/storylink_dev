import { reverse } from "named-urls";

class ManagerURL {
  private domainURL: string;

  /**
   *
   * @param backendURL need trail slash ('.com/' instead '.com').
   */
  constructor(backendURL: string) {
    this.domainURL = backendURL;
  }

  public getAbsolutePath(url: string, params: JSON = JSON.parse("{}")) {
    let relativePath = reverse(url, params);
    if (relativePath.startsWith("/")) {
      relativePath = relativePath.slice(1);
    }
    let absolutePath = `${this.domainURL}${relativePath}`;
    return absolutePath;
  }

  public getRelativePath(url: string, params: JSON = JSON.parse("{}")) {
    let relativePath = reverse(url, params);
    return relativePath;
  }
}

export default ManagerURL;
