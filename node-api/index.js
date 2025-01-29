const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
app.use(cors());

const quotes = [
    'Keep pushing forward! 🚀',
    'Success is the sum of small efforts repeated daily. 🔥',
    'The best way to predict the future is to create it. 💡',
    'Believe in yourself and all that you are. 🌟',
    `Don't stop when you're tired. Stop when you're done. 🏆`,
    'Dream it. Wish it. Do it. 🙌',
]

app.get('/', (req, res) => {
    res.json({
        email: process.env.EMAIL,
        current_datetime: new Date().toISOString().split('.')[0] + 'Z',
        github_url: 'https://github.com/CynthiaWahome/basic-public-api',
        track: 'Backend',
        server_info: {
            os: process.platform,
            node_version: process.version,
        },
        message: quotes[Math.floor(Math.random() * quotes.length)],
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
