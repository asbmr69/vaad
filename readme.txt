# 🚀 Founder Connect - Real-time Chat & Forum for Founders

A real-time web application built with FastAPI that enables founders, co-founders, and investors to connect, share challenges, lessons, and find opportunities.

![Founder Connect](https://img.shields.io/badge/FastAPI-0.104-green) ![WebSocket](https://img.shields.io/badge/WebSocket-Enabled-blue) ![Responsive](https://img.shields.io/badge/Mobile-Responsive-purple)

## ✨ Features

- **💬 Real-time Global Chat** - Instant messaging with WebSocket technology
- **📋 Thread System** - Create and participate in discussion threads
- **🏷️ Categories** - Organized by Funding, Lessons, Challenges, and Opportunities
- **👤 Temporary Profiles** - Auto-generated user IDs (no signup required)
- **💾 Persistent Threads** - Threads and messages remain available
- **📱 Fully Responsive** - Optimized for mobile and desktop
- **🔴 Live User Count** - See active users in real-time
- **⚡ Lightning Fast** - Built on FastAPI for maximum performance

## 🎯 Use Cases

- **💰 Funding**: Share investment needs and connect with investors
- **📚 Lessons**: Share startup lessons and experiences
- **⚡ Challenges**: Discuss obstacles and get community support
- **🎯 Opportunities**: Post job openings, partnerships, and collaboration opportunities

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **WebSocket**: Real-time bidirectional communication
- **Frontend**: HTML5, JavaScript (Vanilla), Tailwind CSS
- **Deployment**: Render.com / Railway / Heroku ready

## 📦 Quick Start

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/founder-connect.git
cd founder-connect
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

4. **Open your browser**
```
http://localhost:8000
```

### Using uvicorn directly
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 🚀 Deploy to Render.com

1. **Push code to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/founder-connect.git
git push -u origin main
```

2. **Deploy on Render**
   - Go to [Render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Click "Create Web Service"

3. **Your app is live!** 🎉

## 📁 Project Structure

```
founder-connect/
├── main.py              # FastAPI backend with WebSocket
├── index.html           # Responsive frontend
├── requirements.txt     # Python dependencies
└── README.md           # Documentation
```

## 🎨 Screenshots

### Desktop View
- Split-screen layout with thread sidebar and main content area
- Real-time global chat with message history
- Thread creation with category selection

### Mobile View
- Collapsible sidebar with smooth animations
- Optimized touch interactions
- Full-featured mobile experience

## 🔧 Configuration

### Environment Variables (Optional)

```bash
PORT=8000                    # Server port
CORS_ORIGINS=*              # CORS allowed origins
```

## 🌟 Key Features Explained

### Temporary User Profiles
- Each user gets a unique ID generated on connection
- No signup or authentication required for MVP
- Profile is deleted when user closes browser/tab

### Thread System
- Create threads in 4 categories
- Real-time updates when new threads are posted
- Reply to any thread with instant updates
- View all replies in chronological order

### Global Chat
- Real-time messaging for quick discussions
- Message history persists during server uptime
- User indicators show who's speaking

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Serve main HTML page |
| GET | `/api/threads` | Get all threads |
| POST | `/api/threads` | Create new thread |
| GET | `/api/threads/{id}` | Get specific thread |
| POST | `/api/threads/{id}/reply` | Reply to thread |
| GET | `/api/chat/messages` | Get chat history |
| GET | `/api/stats` | Get system statistics |
| WS | `/ws/{user_id}` | WebSocket connection |

## 🔐 Security Considerations

Current MVP includes:
- ✅ HTML escaping to prevent XSS
- ✅ CORS middleware configured
- ✅ Input validation with Pydantic

For production, add:
- 🔒 User authentication (JWT)
- 🔒 Rate limiting
- 🔒 Content moderation
- 🔒 Database with proper indexing
- 🔒 HTTPS enforcement

## 📈 Scaling for Production

### Add Database Persistence

Install PostgreSQL support:
```bash
pip install sqlalchemy psycopg2-binary
```

Update `requirements.txt` and modify `main.py` to use database instead of in-memory storage.

### Add Redis for Sessions

```bash
pip install redis aioredis
```

Use Redis for WebSocket pub/sub across multiple server instances.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License

MIT License - feel free to use this project for your needs.

## 💡 Future Enhancements

- [ ] User authentication (OAuth, JWT)
- [ ] User profiles with avatars
- [ ] Direct messaging between users
- [ ] File/image uploads in threads
- [ ] Email notifications
- [ ] Advanced search and filtering
- [ ] Admin moderation panel
- [ ] Thread voting/reactions
- [ ] Bookmarks and favorites
- [ ] Mobile apps (React Native)

## 🐛 Known Issues

- In-memory storage means data resets on server restart
- Free tier on Render.com sleeps after 15 mins of inactivity
- No message edit/delete functionality yet

## 📞 Support

For questions or support:
- Open an issue on GitHub
- Check the deployment guide
- Review FastAPI documentation

---

**Built with ❤️ for the founder community**

Start connecting, sharing, and growing together! 🚀