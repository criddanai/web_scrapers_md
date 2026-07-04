# Structure Project

run --> python main_urls.py

ai-docs-rag/
│
├── .env
├── requirements.txt
├── README.md
│
├── input_urls.txt
│
├── main.py
├── main_urls.py
│
├── build_vectors.py
├── chat.py
│
├── core/
│   ├── __init__.py
│   │
│   ├── crawler.py
│   ├── fetcher.py
│   ├── extractor.py
│   ├── cleaner.py
│   ├── exporter.py
│   │
│   ├── book_builder.py
│   └── chunker.py
│
├── output/
│   │
│   ├── urls.txt
│   │
│   ├── md/
│   │   ├── docs_nxlog_windows-event-log.md
│   │   ├── docs_nxlog_gelf.md
│   │   ├── docs_nxlog_language.md
│   │   ├── graylog_opensearch.md
│   │   ├── graylog_configuration.md
│   │   ├── telegram_sendmessage.md
│   │   ├── securitylog_4625.md
│   │   ├── securitylog_4720.md
│   │   └── securitylog_1102.md
│   │
│   ├── books/
│   │   ├── book_001.md
│   │   └── book_002.md
│   │
│   └── chunks/
│       └── chunks.jsonl
│
├── vector_db/
│
└── logs/



