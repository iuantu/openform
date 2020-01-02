const baseURL = "http://localhost:5000"

class UILogin {
    constructor(json) {
        if (json.hasOwnProperty("message")) {
            this.isSuccess = false;
            this.message = json.message;
        } else {
            this.isSuccess = true;

            localStorage.setItem('access_token', json.access_token);
            localStorage.setItem('refresh_token', json.refresh_token);
        }
    }

    isSuccess() {
        return this.isSuccess;
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
        if (401 == response.status) {
            // no implement
        }
        return response
    }
}