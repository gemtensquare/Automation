import url from "./BaseURL";


let baseUrl = url.baseUrl;
let mediaBaseUrl = url.mediaBaseUrl;


const API = {
    baseUrl: baseUrl,
    mediaBaseUrl: mediaBaseUrl,
    testApi: `${baseUrl}/test/`,
    getNews: `${baseUrl}/news/`,
    PostNews: `${baseUrl}/post/to/facebook/`,
    getTemplate: `${baseUrl}/template/`
};


export default API;