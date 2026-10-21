require('../scss/styles.scss');

const bootstrap = require('bootstrap');

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

const toastTrigger = document.getElementById('liveToastBtn')
const liveToastTemplate = document.getElementById('liveToast')
const container = document.getElementById('toastContainer')

if (toastTrigger) {
    toastTrigger.addEventListener('click', () => {
        if (container.children.length > 3) return;
        const newToast = liveToastTemplate.cloneNode(true);
        newToast.style.display = '';
        container.appendChild(newToast);
        const bsToast = new bootstrap.Toast(newToast);
        bsToast.show();
        newToast.addEventListener("hidden.bs.toast", () => {
            newToast.remove();
        })
    })
}

const maxModals = 5;

let isTransitioning = false;

document.addEventListener("keydown", (event) => {
    if (isTransitioning) return;
    if (event.key !== "ArrowRight" && event.key !== "ArrowLeft") return;

    const openModalRaw = Array.from(document.querySelectorAll('[id^="modal-"]'))
        .find(modal => modal.classList.contains("show"));
    if (!openModalRaw) return;

    const modalId = +openModalRaw.id.split('-')[1];

    let targetId = null;
    if (event.key === "ArrowRight" && modalId < maxModals) targetId = modalId + 1;
    else if (event.key === "ArrowLeft" && modalId > 1) targetId = modalId - 1;
    if (targetId === null) return;

    isTransitioning = true;

    const openModal = bootstrap.Modal.getOrCreateInstance(openModalRaw);
    const nextModal = bootstrap.Modal.getOrCreateInstance(document.getElementById(`modal-${targetId}`));

    openModalRaw.addEventListener("hidden.bs.modal", () => {
        nextModal.show();
    }, { once: true });

    document.getElementById(`modal-${targetId}`).addEventListener("shown.bs.modal", () => {
        isTransitioning = false;
    }, { once: true });

    openModal.hide();
});