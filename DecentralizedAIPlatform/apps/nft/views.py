
from django.shortcuts import render
from .models import NFT

def index(request):
    nfts = NFT.objects.all()
    return render(request, 'nft/index.html', {'nfts': nfts})

def detail(request, nft_id):
    nft = NFT.objects.get(id=nft_id)
    return render(request, 'nft/detail.html', {'nft': nft})
