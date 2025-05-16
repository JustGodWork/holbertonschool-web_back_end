const chai = require("chai");
const request = require("request");

describe("indexPageTest", function () {
  it("Should return status code 200", function (done) {
    request.get("http://localhost:7865", (error, response, body) => {
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(body).to.equal("Welcome to the payment system");

      if (error) return done(error);

      done();
    });
  });
});
