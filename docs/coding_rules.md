# 📝 Coding Rules

## Python Standards

### Style
- PEP 8
- Type hints
- F-strings
- 100 chars max

### Example
```python
def calculate_position_size(capital: float, risk: float) -> float:
    if capital <= 0:
        raise ValueError("Capital must be positive")
    return capital * risk
```

## TypeScript Standards

### Style
- Strict mode
- No `any`
- Interfaces
- Enums

### Example
```typescript
interface Trade {
    id: string;
    symbol: string;
    quantity: number;
    profit: number;
}
```

## Testing

- 85%+ coverage
- Unit tests
- Integration tests
- E2E tests

## Naming

### Python
- Classes: `PascalCase`
- Functions: `snake_case`
- Constants: `UPPER_CASE`

### TypeScript
- Classes: `PascalCase`
- Functions: `camelCase`
- Constants: `UPPER_CASE`

## Git

### Branches
```
feature/name
fix/name
docs/name
test/name
refactor/name
```

### Commits
```
feat: description
fix: description
docs: description
```
