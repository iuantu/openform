const baseURL = "http://localhost:5000"

export async function ofFetch(path = '', options = {}) {
    if (!path.substr(0, 1) == '/') {
        path = '/' + path
    }
    localStorage.setItem('access_token', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzc3Mjc1MDQsIm5iZiI6MTU3NzcyNzUwNCwianRpIjoiODQ2MTZlNTEtYTBhNS00ZTBkLThjNDQtZjA4Njg2YTViMTM1IiwiZXhwIjoxNTc3NzI4NDA0LCJpZGVudGl0eSI6MSwiZnJlc2giOnRydWUsInR5cGUiOiJhY2Nlc3MifQ.WOrGqnCIzV5bvS06X-KpPMzv2EERg4eChGw6lsr89PM')
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