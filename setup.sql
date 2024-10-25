CREATE TABLE users (
    id SERIAL PRIMARY KEY,                -- id列: 自動増分する整数型の主キー
    self_introduction TEXT,               -- self_introduction列: TEXT型
    params_json JSON,                     -- params_json列: JSON型
    is_compile BOOLEAN DEFAULT FALSE      -- is_compile列: BOOLEAN型、デフォルト値はFALSE
);