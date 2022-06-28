const { Router } = require('express');
const File = require('../controllers/files.controller');
const router = Router();

router.get('/', File.getFiles);
router.get('/:fileId', File.getFileById);
router.post('/', File.createFile);
router.put('/:fileId', File.updateFileById);
router.delete('/:fileId', File.deleteFileById);

module.exports = router;