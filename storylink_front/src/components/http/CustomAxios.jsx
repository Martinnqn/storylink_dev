import { create } from "axios";
import { urls as urlDomain } from "../url/URLDomain";

const DOMAIN = "http://dev-storylink.club:8000/";

const axiosApiInstance = create();

axiosApiInstance.interceptors.request.use(
  async (config) => {
    const accessToken = localStorage.getItem("accessToken");
    if (accessToken) {
      config.headers = {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      };
    }
    return config;
  },
  (error) => {
    Promise.reject(error);
  }
);

/**
 * Catch Responses. If the response is 401 and _retry is false/undefined, get
 * new accessToken usign refreshToken and try .
 */
axiosApiInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  async function (error) {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      refreshAccessToken();
      axiosApiInstance.defaults.headers.common["Authorization"] =
        "Bearer " + localStorage.getItem("accessToken");
      return axiosApiInstance(originalRequest);
    }
    return Promise.reject(error);
  }
);

async function refreshAccessToken() {
  const refreshToken = localStorage.getItem("refreshToken");

  const data = await fetch(`${DOMAIN}${urlDomain.token_refresh}`, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: { refresh: refreshToken },
  });

  data.json().then((res) => {
    updateTokens(res);
  });
}

function updateTokens(data) {
  console.log("update with");
  console.log(data);
  localStorage.setItem("refreshToken", data.refresh);
  localStorage.setItem("accessToken", data.access);
}

export default axiosApiInstance;
