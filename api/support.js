export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { name, email, phone, category, message, source } = req.body;

  if (!email || !category || !message) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  try {
    const response = await fetch(
      `${process.env.SUPABASE_URL}/rest/v1/support_tickets`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'apikey': process.env.SUPABASE_SERVICE_ROLE_KEY,
          'Authorization': `Bearer ${process.env.SUPABASE_SERVICE_ROLE_KEY}`,
          'Prefer': 'return=minimal'
        },
        body: JSON.stringify({ name, email, phone, category, message, source: source || 'chat_widget' })
      }
    );

    if (!response.ok) {
      const err = await response.text();
      console.error('Supabase error:', err);
      return res.status(500).json({ error: 'Failed to save ticket' });
    }

    return res.status(200).json({ success: true });
  } catch (err) {
    console.error('Support ticket error:', err);
    return res.status(500).json({ error: 'Internal error' });
  }
}
