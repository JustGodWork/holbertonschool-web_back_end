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

  it("Should return the correct body", function (done) {
    request.get("http://localhost:7865/cart/10", (error, response, body) => {
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(body).to.equal("Payment methods for cart " + 10);
      if (error) return done(error);
      done();
    });
  });

  it("Should work as expected for endpoint GET /available_payements", function (done) {
    request.get("http://localhost:7865/available_payments", (error, response, body) => {
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(body).to.deep.equal('{"payment_methods":{"credit_cards":true,"paypal":false}}');
      if (error) return done(error);
      done();
    });
  })

  it("should work as expected with POST /login endpoint", function (done) {
    request.post("http://localhost:7865/login", { json: { "userName": "Betty" } }, (error, response, body) => {
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(body).to.equal("Welcome Betty");
      if (error) return done(error);
      done();
    });
  })

  it("Should return 404 when id is not numeric", function (done) {
    request.get("http://localhost:7865/cart/hello", (error, response, body) => {
      chai.expect(response.statusCode).to.equal(404);

      if (error) return done(error);
      done();
    });
  });
})
