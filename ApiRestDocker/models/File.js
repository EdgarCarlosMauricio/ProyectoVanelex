var { Schema, model } = require("mongoose");

var FileSchema = Schema({
    input1: {
        type: String,
        required: false,
    },
    input2: {
        type: String,
        required: false,
    },
    input3: {
        type: String,
        required: false,
    },
    input4: {
        type: String,
        required: false,
    },
    input5: {
        type: String,
        required: false,
    },
    input6: {
        type: String,
        required: false,
    },
    input7: {
        type: String,
        required: false,
    },
    input8: {
        type: String,
        required: false,
    },
    input9: {
        type: String,
        required: false,
    },
    input10: {
        type: String,
        required: false,
    },
    
}, {
    timestamps: true,
    versionKey: false,
});

module.exports = model('File', FileSchema);