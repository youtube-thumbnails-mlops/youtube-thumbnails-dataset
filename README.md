# YouTube Thumbnails Dataset

DVC-tracked dataset with automatic batch rotation.

## Structure

```
current/              # Daily collection (max 500 images)
current.dvc           # DVC pointer for current/
batches/
  ├── batch_001/      # Archived batch (500 images)
  ├── batch_001.dvc   # DVC pointer for batch_001/
  ├── batch_002/
  ├── batch_002.dvc   # DVC pointer for batch_002/
  └── ...
```

## DVC Setup

```bash
dvc init
dvc remote add -d origin s3://youtube-thumbnails-dataset
dvc remote modify origin endpointurl https://YOUR_ACCOUNT_ID.r2.cloudflarestorage.com
dvc remote modify origin --local access_key_id YOUR_KEY
dvc remote modify origin --local secret_access_key YOUR_SECRET
```

## Flow

1. Daily: New images → `current/` (varies by filtering)
2. At 500: `current/` → `batches/batch_XXX/`, tag created
3. Tag triggers training

## Related

- [youtube-thumbnails-monorepo](https://github.com/YOUR_ORG/youtube-thumbnails-monorepo) - Collection code
