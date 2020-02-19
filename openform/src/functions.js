export let baseURL;

if (process.env.NODE_ENV === 'development') {
    // baseURL = `${document.location.protocol}//${document.location.hostname}:5000`;
    baseURL = 'https://staging.oform.cn'
} else {
    baseURL = `${document.location.protocol}//${document.location.host}`;
}

class UIBase {
    constructor(json) {
        if (json.hasOwnProperty("message")) {
            this.isSuccess = false;
            this.message = json.message;
        } else {
            this.isSuccess = true;
        }
    }

    isSuccess() {
        return this.isSuccess;
    }
}

class UILogin extends UIBase {
    constructor(json) {
        super(json);

        if (super.isSuccess) {
            localStorage.setItem('access_token', json.access_token);
            localStorage.setItem('refresh_token', json.refresh_token);
        }
    }
}

class UIRegister extends UIBase {
    constructor(json) {
        super(json);
        
        if (this.isSuccess) {
            localStorage.setItem('access_token', json.jwt.access_token);
            localStorage.setItem('refresh_token', json.jwt.refresh_token);
        }
    }
}

class HttpClient {
    async request(path, options) {
        return ofFetch(path, options);
    }
}

export class SecurityService {
    constructor() {
        this.client = new HttpClient();
    }

    async login(username, password) {
        const response = await this.client.request(
            '/api/v1/security/login',
            {
                method: 'POST',
                body: JSON.stringify({
                    "password": password,
                    "provider": "db",
                    "refresh": true,
                    "username": username,
                })
            }
        );
        const json = await response.json();
        return new UILogin(json);
    }

    async register(username, email, password) {
        const response = await this.client.request(
            '/api/v1/user/',
            {
                method: 'POST',
                body: JSON.stringify({
                    "password": password,
                    "email": email,
                    "username": username,
                })
            }
        );
        const json = await response.json();
        return new UIRegister(json);
    }

    async getFormList(){
        const response = await this.client.request(
            '/api/v1/cp/form/',
            {
                method: 'GET',
            }
        )
        const json = await response.json()
        return json
    }

    async postApi(url, postData){
        const response = await this.client.request(
            '/api/v1/' + url,
            {
                method: 'POST',
                body: JSON.stringify(postData)
            }
        )
        const json = await response.json()
        return json
    }

    async getApi(url){
        const response = await this.client.request(
            '/api/v1/' + url,
            {
                method: 'GET'
            }
        )
        const json = await response.json()
        return json
    }

    async putApi(url, postData){
        const response = await this.client.request(
            '/api/v1/' + url,
            {
                method: 'PUT',
                body: JSON.stringify(postData)
            }
        )
        const json = await response.json()
        return json
    }
}

export async function ofFetch(path = '', options = {}) {

    if (!path.substr(0, 1) == '/') {
        path = '/' + path
    }
    
    const access_token = localStorage.getItem("access_token")
    if (!options.headers) {
        options.headers = {}
    }
    options.headers['Content-Type'] = 'application/json';
    options.headers.Authorization = `Bearer ${access_token}`

    for (let i = 0; i < 3; i++ ) {
        const response = await fetch(baseURL + path, options)
        // const response = await fetch(path, options)
        if (401 == response.status) {
            // no implement
        }
        return response
    }
}