const File = require('../models/File');


// Search all files
const getFiles = async function (req, res) {
    try {
        const archivos = await File.find();
        return res.status(201).json(archivos);
    } catch (error) {
        return res.status(500).json({ msg: 'Por favor hable con el administrador' });
    }

};

//Search for a specific file
const getFileById = async function (req, res) {
    try {
        const archivo = await File.findById(req.params.fileId);
        return res.status(201).json(archivo);
    } catch (error) {
        return res.status(500).json({ msg: 'Id Del archivo No Existe' });
    }
};

//Update file simply
const updateFileById = async function (req, res) {
    let r = req.body;
    try {
        const archivo = await File.findByIdAndUpdate(req.params.fileId, r, { new: true });
        return res.status(200).json(archivo);
    } catch (error) {
        return res.status(500).json({ msg: 'Id De Archivo No Existe' });
    }
};

//Add - Update missing file data
const createFile = async function (req, res) {
    let r = req.body.data;
    try {
        const newFile = new File(r);
        await newFile.save();
        return res.status(201).json({ msg: 'Archivo Guardado' });
    } catch (error) {
        return res.status(500).json({ msg: 'Error Al Guardar Archivo' });
    }
};


//Delete a file
const deleteFileById = async function (req, res) {
    try {
        await File.findByIdAndDelete(req.params.fileId);
        return res.status(201).json({ msg: 'Archivo Borrado Con Exito' });
    } catch (error) {
        return res.status(500).json({ msg: 'Id De Archivo No Existe' });
    }
};



module.exports = {
    getFiles,
    getFileById,
    deleteFileById,
    updateFileById,
    createFile
}