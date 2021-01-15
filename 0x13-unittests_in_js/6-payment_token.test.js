const { expect, assert } = require('chai');
const sinon = require('sinon');

const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
    it('promise response from API should resolve', (done) => {
        getPaymentTokenFromAPI(true)
        .then((response) => {
            expect(response).to.eql({ data: 'Successful response from the API' });
            done();
        })
        .catch((err) => {
            done(err);
        });
    });
});
