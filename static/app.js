document.addEventListener('DOMContentLoaded', () => {
    const scanBtn = document.getElementById('scan-btn');
    const targetInput = document.getElementById('target-input');
    const logsContainer = document.getElementById('logs-container');
    const totalScannedEl = document.getElementById('total-scanned');
    const totalLeaksEl = document.getElementById('total-leaks');

    let isScanning = false;

    // Fetch initial data
    updateDashboard();

    // Set up polling for real-time monitoring feel
    setInterval(() => {
        if (!isScanning) {
            updateDashboard();
        }
    }, 5000);

    scanBtn.addEventListener('click', async () => {
        if (isScanning) return;

        const query = targetInput.value.trim();
        isScanning = true;
        scanBtn.textContent = 'Searching...';
        scanBtn.disabled = true;

        try {
            const url = query ? `/api/scan?query=${encodeURIComponent(query)}` : '/api/scan';
            const response = await fetch(url);
            const data = await response.json();

            // Artificial delay for UX
            setTimeout(() => {
                updateDashboard();
                isScanning = false;
                scanBtn.textContent = 'Manual Scan Feed';
                scanBtn.disabled = false;
            }, 800);
        } catch (error) {
            console.error('Scan failed:', error);
            isScanning = false;
            scanBtn.textContent = 'Manual Scan Feed';
            scanBtn.disabled = false;
        }
    });

    async function updateDashboard() {
        try {
            const response = await fetch('/api/dashboard');
            const data = await response.json();

            totalScannedEl.textContent = data.total_scanned;
            totalLeaksEl.textContent = data.total_leaks;

            if (data.leaks.length > 0) {
                renderLogs(data.leaks);
            }
        } catch (error) {
            console.error('Update failed:', error);
        }
    }

    function renderLogs(leaks) {
        // Reverse to show newest on top
        const sortedLeaks = [...leaks].reverse();

        logsContainer.innerHTML = sortedLeaks.map(leak => `
            <div class="leak-item">
                <div class="leak-header">
                    <span class="platform-tag">${leak.post.platform} • @${leak.post.user}</span>
                    <span class="timestamp">${leak.post.timestamp}</span>
                </div>
                <div class="leak-content">
                    ${leak.post.content}
                </div>
                <div class="findings">
                    ${leak.findings.map(f => `
                        <span class="finding-pill">Detected: ${f.type.toUpperCase()}</span>
                    `).join('')}
                    <span class="finding-pill" style="background: rgba(255,255,255,0.1); color: white;">Severity: ${leak.severity}</span>
                </div>
            </div>
        `).join('');
    }
});
