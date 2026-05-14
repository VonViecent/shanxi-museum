const API_BASE = 'http://localhost:5000/api';

// Load data on page load
document.addEventListener('DOMContentLoaded', () => {
    loadArtifacts();
    loadExhibitions();
});

// Artifact functions
function loadArtifacts() {
    fetch(`${API_BASE}/artifacts`)
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById('artifact-list');
            list.innerHTML = '';
            data.forEach(item => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <strong>${item.name}</strong> - ${item.description || ''} (${item.age || ''}, ${item.origin || ''})
                    <button class="edit-btn" onclick="editArtifact(${item.id})">编辑</button>
                    <button class="delete-btn" onclick="deleteArtifact(${item.id})">删除</button>
                `;
                list.appendChild(li);
            });
        });
}

document.getElementById('artifact-form').addEventListener('submit', e => {
    e.preventDefault();
    const data = {
        name: document.getElementById('artifact-name').value,
        description: document.getElementById('artifact-description').value,
        age: document.getElementById('artifact-age').value,
        origin: document.getElementById('artifact-origin').value
    };
    fetch(`${API_BASE}/artifacts`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    }).then(() => {
        loadArtifacts();
        e.target.reset();
    });
});

function editArtifact(id) {
    // Simple edit: prompt for new name
    const newName = prompt('新名称:');
    if (newName) {
        fetch(`${API_BASE}/artifacts/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: newName })
        }).then(() => loadArtifacts());
    }
}

function deleteArtifact(id) {
    fetch(`${API_BASE}/artifacts/${id}`, { method: 'DELETE' })
        .then(() => loadArtifacts());
}

// Exhibition functions
function loadExhibitions() {
    fetch(`${API_BASE}/exhibitions`)
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById('exhibition-list');
            list.innerHTML = '';
            data.forEach(item => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <strong>${item.title}</strong> - ${item.description || ''} (${item.start_date} to ${item.end_date})
                    <button class="edit-btn" onclick="editExhibition(${item.id})">编辑</button>
                    <button class="delete-btn" onclick="deleteExhibition(${item.id})">删除</button>
                `;
                list.appendChild(li);
            });
        });
}

document.getElementById('exhibition-form').addEventListener('submit', e => {
    e.preventDefault();
    const data = {
        title: document.getElementById('exhibition-title').value,
        description: document.getElementById('exhibition-description').value,
        start_date: document.getElementById('exhibition-start-date').value,
        end_date: document.getElementById('exhibition-end-date').value
    };
    fetch(`${API_BASE}/exhibitions`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    }).then(() => {
        loadExhibitions();
        e.target.reset();
    });
});

function editExhibition(id) {
    const newTitle = prompt('新标题:');
    if (newTitle) {
        fetch(`${API_BASE}/exhibitions/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: newTitle })
        }).then(() => loadExhibitions());
    }
}

function deleteExhibition(id) {
    fetch(`${API_BASE}/exhibitions/${id}`, { method: 'DELETE' })
        .then(() => loadExhibitions());
}