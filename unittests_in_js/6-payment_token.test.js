const chai = require("chai");
const getPaymentTokenFromAPI = require("./6-payment_token.js");

describe("getPaymentTokenFromAPI", function () {
  it("should return a resolved promise with correct data when success is true", function (done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        chai.expect(response).to.deep.equal({
          data: "Successful response from the API",
        });
        done();
      })
      .catch((error) => done(error));
  });
});
