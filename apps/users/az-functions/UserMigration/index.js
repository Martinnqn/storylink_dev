module.exports = async function (context, req) {
    const sql = require('mssql');
    console.log("pasaaaa");
    const config = {
        user: 'sa',
        password: '12345',
        server: 'localhost', // You can use 'localhost\\instance' to connect to named instance
        database: 'st-main',
    }

    context.log("JavaScript HTTP trigger function processed a request v1.");
    const API_VERSION = "1.0.0";
  
    // parse Basic Auth username and password
   /* var header = req.headers["authorization"] || "", // get the header
      token = header.split(/\s+/).pop() || "", // and the encoded auth token
      auth = new Buffer.from(token, "base64").toString(), // convert from base64
      parts = auth.split(/:/), // split on colon
      username = parts[0],
      password = parts[1];
  
    // Check for HTTP Basic Authentication, return HTTP 401 error if invalid credentials.
    if (
      username !== process.env["BASIC_AUTH_USERNAME"] ||
      password !== process.env["BASIC_AUTH_PASSWORD"]
    ) {
      context.res = {
        status: 401,
      };
      context.log("Invalid Authentication");
      return;
    }*/
  var asd=0;
    try {
        let pool = await sql.connect(config)

        let result2 = await pool.request()
            .input('input', sql.Int, 5)
            .output('output', sql.Int)
            .execute('testCallSP')
        
        console.dir(result2)
        asd = result2;
    } catch (err) {
        // ... error checks
        console.log(err)
    }
  
    context.res = {
      body: { version: API_VERSION, action: "Continue", value: asd.returnValue },
    };
  
    context.log(context.res);
    return;
  };