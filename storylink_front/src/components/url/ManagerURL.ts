import { reverse } from 'named-urls'

class ManagerURL {
    baseUrl: string;

    constructor(baseUrl: string) {
        this.baseUrl = baseUrl;
    }

    getPath(url: string, params?: JSON) {
        return reverse(url, params);
    }

}

export default ManagerURL;