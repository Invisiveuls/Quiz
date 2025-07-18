button1.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        final String texto = edittext1.getText().toString();

        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    java.net.URL url = new java.net.URL("https://flask-ozz6.onrender.com/gemini");
                    javax.net.ssl.HttpsURLConnection conn = (javax.net.ssl.HttpsURLConnection) url.openConnection();
                    conn.setRequestMethod("POST");
                    conn.setRequestProperty("Content-Type", "application/json; charset=UTF-8");
                    conn.setDoOutput(true);

                    String jsonBody = "{\"text\":\"" + texto.replace("\"", "\\\"") + "\"}";
                    java.io.OutputStream os = conn.getOutputStream();
                    os.write(jsonBody.getBytes("UTF-8"));
                    os.flush();
                    os.close();

                    java.io.BufferedReader br = new java.io.BufferedReader(new java.io.InputStreamReader(conn.getInputStream(), "UTF-8"));
                    final StringBuilder sb = new StringBuilder();
                    String line;
                    while ((line = br.readLine()) != null) {
                        sb.append(line);
                    }
                    br.close();
                    conn.disconnect();

                    final String resposta = sb.toString();

                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            try {
                                String[] partes = resposta.split("\"resposta\":\\s*\"");
                                String textoResposta = (partes.length > 1) ? partes[1].split("\"")[0] : "Resposta inválida";
                                textview1.setText(textoResposta);
                            } catch (Exception e) {
                                textview1.setText("Erro ao interpretar resposta");
                            }
                        }
                    });
                } catch (final Exception e) {
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            textview1.setText("Erro: " + e.toString());
                        }
                    });
                }
            }
        }).start();
    }
});
