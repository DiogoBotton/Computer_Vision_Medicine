# Build
FROM node:20-slim

RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app

COPY package.json pnpm-lock.yaml ./

# Instalar dependências
RUN pnpm install

COPY . .

# Expor a porta do Vite padrão
EXPOSE 5173

# Rodar o servidor de desenvolvimento
CMD ["pnpm", "run", "dev", "--host", "0.0.0.0"]
