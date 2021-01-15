const { expect, assert } = require('chai');
const sinon = require('sinon');
const { spy } = require('sinon');

const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
    let spy;

    beforeEach(() => { 
        spy = sinon.spy(console, 'log');
    });

    afterEach(() => { 
        spy.restore();
    })

    it('should log correct output of calculateNumber(100, 20)', () => {
        sendPaymentRequestToApi(100, 20);
        expect(spy.calledOnceWithExactly('The total is: 120')).to.be.true;
        expect(spy.calledOnce).to.be.true;
    });

    it('should log correct output of calculateNumber(10, 10)', () => {
        sendPaymentRequestToApi(10, 10);
        expect(spy.calledOnceWithExactly('The total is: 20')).to.be.true;
        expect(spy.calledOnce).to.be.true;
    });
});
