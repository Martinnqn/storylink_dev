async function request(path, method, body) {
  const user = localStorage.getItem("user");
  const headers = {
    Authentication: `Token ${user.token}`,
  };

  const url = path; // add logic to get correct url for the environment

  const response = await fetch(url, { method, body, headers });

  // add response handling
  // - session management
  // - convert to correct data type - response.json(), etc
  // - handle common errors like 401, 403 etc

  return response;
}

export default request;
