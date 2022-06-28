const mongoose = require('mongoose');

const dbConnection = async function () {
    try {
        await mongoose.connect(process.env.BD_CNN, {
            useNewUrlParser: true,
            useUnifiedTopology: true
        });
        console.log('BD Online', process.env.BD_CNN);
        // mongoose.set('useFindAndModify', false);
    } catch (error) {
        console.log(error);
        throw new Error('Error a la hora de inicializar DB');
    }
}

module.exports = {
    dbConnection
}