const baseURL = "http://localhost:5000"

export async function ofFetch(path = '', options = {}) {
    if (!path.substr(0, 1) == '/') {
        path = '/' + path
    }
    localStorage.setItem('access_token', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzc3NTUxODUsIm5iZiI6MTU3Nzc1NTE4NSwianRpIjoiMTY4MDI5NTUtY2NjYy00Nzg4LWI2Y2ItOTliNTNmNzZkYTQ0IiwiZXhwIjoxNjA5MjkxMTg1LCJpZGVudGl0eSI6MSwiZnJlc2giOnRydWUsInR5cGUiOiJhY2Nlc3MifQ.Y3vHYELJAQzMN--Y9aKVNdnEh2fCxhlyr38WPhDanwE')
    localStorage.setItem('refresh_token', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzc3MjU1MDgsIm5iZiI6MTU3NzcyNTUwOCwianRpIjoiYmJkNzE1OTctZDM3Mi00ZmMwLWEwMTAtMjZkMTllMzllZGUxIiwiZXhwIjoxNTgwMzE3NTA4LCJpZGVudGl0eSI6MSwidHlwZSI6InJlZnJlc2gifQ.34bcFCal3P7nWPaOEZoCeUkU7Wl2iJtJTGOOo3AU2VM')

    const access_token = localStorage.getItem("access_token")
    if (!options.headers) {
        options.headers = {}
    }
    options.headers.Authorization = `Bearer ${access_token}`

    for (let i = 0; i < 3; i++ ) {
        const response = await fetch(baseURL + path, options)
        if (401 == response.status) {
            // no implement
        }
        return response
    }
}