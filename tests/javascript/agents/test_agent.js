
const assert = require('assert');
const Agent = require('../../src/javascript/agents/agent.js');

describe('Agent', function() {
  describe('#download()', function() {
    it('should download without error', function(done) {
      Agent.download(function(err) {
        if (err) done(err);
        else done();
      });
    });
  });

  describe('#execute()', function() {
    it('should execute without error', function(done) {
      Agent.execute(function(err) {
        if (err) done(err);
        else done();
      });
    });
  });

  describe('#update()', function() {
    it('should update without error', function(done) {
      Agent.update(function(err) {
        if (err) done(err);
        else done();
      });
    });
  });
});
