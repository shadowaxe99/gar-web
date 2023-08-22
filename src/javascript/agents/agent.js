
const axios = require('axios');

class Agent {
    constructor(agentId, agentLanguage) {
        this.agentId = agentId;
        this.agentLanguage = agentLanguage;
    }

    async downloadAgent() {
        try {
            const response = await axios.get(`http://localhost:3000/agents/${this.agentId}`);
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }

    async updateAgentLanguage(newLanguage) {
        try {
            const response = await axios.put(`http://localhost:3000/agents/${this.agentId}`, {
                language: newLanguage
            });
            this.agentLanguage = newLanguage;
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }
}

module.exports = Agent;
