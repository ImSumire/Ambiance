Symbols representing cardinalities in the schema:

| Symbols  | Cardinality |
|----------|-------------|
| o\|      | 0, 1        |
| o}       | 0, n        |
| \|       | 1, 1        |
| \|}      | 1, n        |




```mermaid
erDiagram
    GENRE {
        int id PK
        varchar name
    }

    ALBUM {
        int id PK
        varchar title
    }
    ALBUM }|..o{ ARTIST : "Is produced by"
    
    ARTIST {
        int id PK
        varchar name
        varchar last_name
    }

    SONG {
        int id PK
        varchar title
        time length
        date creation
    }
    SONG }o..|{ GENRE : "Is defined by"
    SONG }|..|{ ALBUM : "Is a part of"

    USER {
        int id PK
        varchar name
        varchar last_name
        date birth
    }
    USER ||..|{ CONTRACT : "Is registered under"
    
    CONTRACT {
        int id PK
        date start
        date end
        int capacity
    }

    ACTIVITY {
        int id PK
        date start
        int elapsed
    }
    ACTIVITY ||..o{ USER : "Is tied to"
    ACTIVITY ||..o{ SONG : "Is tied to"
```
