const express = require('express');
const cors = require('cors');
const path = require('path');
const { spawn } = require('child_process');

const app = express();
app.use(cors());
app.use(express.json());

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Health check
app.get('/health', (_req, res) => res.json({ ok: true }));

// Chat API -> calls Python chatbot.py
app.post('/api/chat', async (req, res) => {
  const { message, history = [] } = req.body || {};
  if (!message || typeof message !== 'string') {
    return res.json({ reply: '' });
  }

  // Gọi lại chatbot.py
  const pyBin = process.env.PYTHON_BIN || 'python';
  const script = path.join(__dirname, 'chatbot.py');
  let result = '';
  try {
    const env = { ...process.env };
    const py = spawn(pyBin, [script, message], { env });

    py.stdout.on('data', (data) => { result += data.toString(); });
    py.stderr.on('data', (data) => { console.error('[chatbot.py]', data.toString()); });

    py.on('close', (_code) => {
      res.json({ reply: (result || '').trim() });
    });
  } catch (err) {
    console.error('Spawn error:', err);
    res.json({ reply: 'Lỗi server hoặc không gọi được chatbot.' });
  }
});

// Fallback to index.html for root
app.get('/', (_req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`✅ Server running: http://localhost:${PORT}`);
});
