-- kitenga - whakapapa of memory loops
CREATE TABLE memory_loops (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  context JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

-- kitenga - agent registry
CREATE TABLE kaitiaki_registry (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  personality TEXT,
  whakapapa JSONB,
  activated_at TIMESTAMP DEFAULT NOW()
);