import { getMeta } from "./components/fields";

export let baseURL;

if (process.env.NODE_ENV === 'development') {
    baseURL = `${document.location.protocol}//${document.location.hostname}:5000`;
    // baseURL = 'https://staging.oform.cn'
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

class BaseService {
    constructor() {
        this.client = new HttpClient();
    }
}

export class FormService extends BaseService {
    async fetchForm(formId) {
        const response = await this.client.request(
            `/api/v1/cp/form/${formId}`
        );
        const json = await response.json();

        return json;
    }

    async changeForm(formId, request) {
        const response = await this.client.request(
            `/api/v1/cp/form/${formId}`,
            {
                method: 'PUT',
                body: JSON.stringify(request)
            }
        );
        const json = await response.json();

        return json;
    }

    async createForm(request) {
        const response = await this.client.request(
            `/api/v1/cp/form`,
            {
                method: 'POST',
                body: JSON.stringify(request)
            }
        );
        const json = await response.json();

        return json;
    }

    async fetchValue(valueId) {
        const response = await this.client.request(
            `/api/v1/form/0/${valueId}`
        );
        return await response.json();
    }

    async submit(formId, valueId, fields) {
        let url;
        if (valueId > 0) {
            url = `/api/v1/cp/form/${formId}/${valueId}`
        } else {
            url = `/api/v1/cp/form/${formId}`
        }

        const request = {}
        fields.forEach((field) => {
            const meta = getMeta(field.discriminator);
            request[field.id] = meta.assembler.toFormValueForRequest(field);
        });
        console.log(request);

        // const response = await this.client.request(
        //     url,
        //     {
        //         method: valueId > 0 ? 'PUT' : 'POST',
        //         body: JSON.stringify(request)
        //     }
        // );
        // return await response.json();
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
        if (401 === response.status) {
            // no implement
        } else if (422 === response.status) {
            document.location = "/#/login";
        }
        return response
    }
}